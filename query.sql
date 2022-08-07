SELECT product.id, product.name, product.price, product.visibility
FROM product
LEFT OUTER JOIN catalog_products ON (product.id = catalog_products.product_id)
WHERE (
	catalog_products.catalog_id IN (
		SELECT catalog.id
		FROM catalog
		INNER JOIN buyer_catalogs ON (catalog.id = buyer_catalogs.catalog_id)
		WHERE buyer_catalogs.buyer_id = 1
	)
	OR product.visibility = 1
)