import splitfolders

input_folder = 'C:\\Users\\Hp\\Desktop\\DSprojects\\8.Potato_disease\\training\\Plantvillage'

output_folder = 'C:\\Users\\Hp\\Desktop\DSprojects\\8.Potato_disease\\training\data'

splitfolders.ratio(input_folder, output=output_folder, seed=42, ratio=(0.7, 0.1, 0.2))
