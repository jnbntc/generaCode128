import barcode
from barcode import Code128

with open('usuarios.txt', 'r') as file:
    for line in file:
        word = line.strip()
        code = Code128(word, writer=barcode.writer.ImageWriter())
        code.default_writer_options['module_width'] = 0.4
        code.default_writer_options['module_height'] = 15
        code.default_writer_options['write_text'] = False
        code.save(word)

print("Todos los códigos de barras se han generado con éxito.")
