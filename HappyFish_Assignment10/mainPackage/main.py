# Name: Group HappyFish (Quynh Doan, Denise Huynh, Sarah Mahan)
# email: doanqb@mail.uc.edu, huynhd2@mail.uc.edu, mahansa@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: 11/07/2024 
# Course #/Section: IS 4010-001
# Semester/Year: Fall Semester 2024
# Brief Description of the assignment: In this assignment you will work in teams to develop a VS project that accesses our SQL Server instance, extracts some data from the Grocery Store Simulator database, and produces some interesting results
# Brief Description of what this module does: This Python module connects to a database and executes SQL queries to fetch product information, including the product description, manufacturer, brand, and the number of items sold. It randomly selects a product from the tProduct table, retrieves the corresponding manufacturer and brand details, and calculates the total sales for that product. Finally, the module prints a grammatically correct sentence summarizing the product's details and sales data.
# Citations: N/A
# Anything else that's relevant: N/A

# main.py

import random
from dbUtilitiesPackage.dbUtilities import connect_to_database
from queryUtilitiesPackage.queryUtilities import fetch_query_results

if __name__ == "__main__":
    # Step 1: Connect to the database and fetch product data
    product_query = "SELECT ProductID, [UPC-A ], Description, ManufacturerID, BrandID FROM tProduct"
    product_data = fetch_query_results(product_query)
    
    # Check if product data was fetched
    if not product_data:
        print("No product data found or query returned no data.")
    else:
        # Step 2: Randomly select a product
        selected_product = random.choice(product_data)
        product_id = selected_product[0]
        description = selected_product[2] if selected_product[2] else "Unknown Product"  # Fallback if Description is empty
        manufacturer_id = selected_product[3]
        brand_id = selected_product[4]

        # Step 3 & 4: Fetch Manufacturer name
        manufacturer_query = f"SELECT Manufacturer FROM tManufacturer WHERE ManufacturerID = {manufacturer_id}"
        manufacturer_data = fetch_query_results(manufacturer_query)
        if manufacturer_data:
            manufacturer_name = manufacturer_data[0][0]
        else:
            print(f"No manufacturer found for ManufacturerID {manufacturer_id}.")
            manufacturer_name = "Unknown Manufacturer"

        # Step 5: Fetch Brand name
        brand_query = f"SELECT Brand FROM tBrand WHERE BrandID = {brand_id}"
        brand_data = fetch_query_results(brand_query)
        if brand_data:
            brand_name = brand_data[0][0]
        else:
            print(f"No brand found for BrandID {brand_id}.")
            brand_name = "Unknown Brand"

        # Step 6: Fetch the number of items sold for the selected product
        sales_query = f"""
        SELECT TOP (100) PERCENT SUM(dbo.tTransactionDetail.QtyOfProduct) AS NumberOfItemsSold
        FROM dbo.tTransactionDetail
        INNER JOIN dbo.tTransaction ON dbo.tTransactionDetail.TransactionID = dbo.tTransaction.TransactionID
        WHERE (dbo.tTransaction.TransactionTypeID = 1) AND (dbo.tTransactionDetail.ProductID = {product_id})
        """
        sales_data = fetch_query_results(sales_query)
        if sales_data:
            number_of_items_sold = sales_data[0][0]
        else:
            print(f"No sales data found for ProductID {product_id}.")
            number_of_items_sold = 0

        # Step 7: Print the result as a grammatically correct sentence
        result_sentence = (
            f"The product '{description}' was manufactured by '{manufacturer_name}' "
            f"under the brand '{brand_name}' and has sold {number_of_items_sold} units."
        )
        print(result_sentence)
