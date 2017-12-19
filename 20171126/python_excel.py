import xlsxwriter

work = xlsxwriter.Workbook("1.xlsx")
worksheet = work.add_worksheet("while")
worksheet.set_column("A:A",20)
bold = work.add_format({"bold":True})
worksheet.write("A1","while",bold)

worksheet.write("A2", 5, bold)
worksheet.write("B2", 8, bold)
worksheet.write("C2","=SUM(A2:B2)",bold)
worksheet.insert_image("A3","C:/Users/nash/Pictures/Saved Pictures/mac/mac01.jpg")

work.close()