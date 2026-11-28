# Calculate Gst...
product_name = str(input("Product Name:"))
product_price = float(input("Enter Product Price:"))
product_quantity = int(input("Enter Product Quantity:"))
gst_rate = float(input("Enter GST Rate:"))
totail_gst = (product_price * product_quantity * gst_rate) / 100
totail_price = (product_price * product_quantity) + totail_gst

print("Product Name:",product_name)
print("Product Price:",product_price)
print("Product Quantity:",product_quantity)
print("GST Rate:",gst_rate,"%")
print("Toatil GST:",totail_gst)
print("Totail Price:",totail_price)


