#main.py

if __name__ == "__main__":
    import pyodbc
    import random
    from dbUtilitiesPackage.dbUtilities import connect_to_database
    from queryUtilitiesPackage.queryUtilities import fetch_query_results

    try:
        # Step 1: Connect to the database
        conn = connect_to_database()
        if conn is None:
            raise Exception("Database connection failed.")  # Error message if connection fails

        # Step 2: Confirm the connection is successful
        print("Database connection successful!")
        
    except Exception as e:
        # Error handling: print the error details and return gracefully
        print("Error accessing the database.")
        print(f"Details: {e}")
    else:

        #1. Submit this query and store the results in a data structure: SELECT ProductID, [UPC-A ], Description, ManufacturerID, BrandID FROM tProduct
        product_query = "SELECT ProductID, [UPC-A ], Description, ManufacturerID, BrandID FROM tProduct"
        print("Executing product query...")  # Debugging info to confirm query is being executed
        product_data = fetch_query_results(product_query)

        # Check if product_data is None or empty
        if not product_data:
            print("No products found or query returned no data.")
        else:
            # Step 4: Store the results in a data structure (a list of tuples)
            # Each tuple contains (ProductID, UPC-A, Description, ManufacturerID, BrandID)
            product_list = product_data  # The fetched data is already a list of tuples
            
            # Step 5: Print the stored data (optional, for debugging purposes)
            print("Product Data Retrieved:")
            for product in product_list:
                print(f"Product ID: {product[0]}, UPC-A: {product[1]}, Description: {product[2]}, Manufacturer ID: {product[3]}, Brand ID: {product[4]}")
            
           
        #2. Randomly select one row from the data structure in step 1. Store the Description in a variable. Store the ProductID in a variable. Store the ManufacturerID and BrandID in variables 
            selected_product = random.choice(product_list)
            
            # Step 6: Store the selected fields in variables
            product_id = selected_product[0]  # ProductID
            description = selected_product[2]  # Description
            manufacturer_id = selected_product[3]  # ManufacturerID
            brand_id = selected_product[4]  # BrandID
            
            # Step 7: Print the selected row's details (for verification)
            print(f"Selected Product: {description} (ProductID: {product_id}, ManufacturerID: {manufacturer_id}, BrandID: {brand_id})")
            
            #3. Using the row from the previous step, build a query using the specific ManufacturerID to look up the manufacturer name.
            manufacturer_query = f"SELECT Manufacturer FROM tManufacturer WHERE ManufacturerID = {manufacturer_id}"
            
            #Execute the query to get the manufacturer name
            manufacturer_data = fetch_query_results(manufacturer_query)

            if not manufacturer_data:
                print(f"No manufacturer found for ManufacturerID {manufacturer_id}.")
            else:
                manufacturer_name = manufacturer_data[0][0]  # Fetch the manufacturer name from the result
                print(f"Manufacturer Name: {manufacturer_name}")
              
            
