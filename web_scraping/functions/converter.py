import csv


def replace_semicolon_with_comma(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        reader = csv.reader(infile, delimiter=';')
        writer = csv.writer(outfile, delimiter=',')

        for row in reader:
            writer.writerow(row)

if __name__ == "__main__":
    input_filename = "../Assoziationsregeln/Assoziations-Decklisten/Colorless.csv"  # Ersetze durch den tatsächlichen Dateinamen
    output_filename = "../Assoziationsregeln/Assoziations-Decklisten/Colorless.csv"  # Name der neuen Datei
    replace_semicolon_with_comma(input_filename, output_filename)
    print(f"Die Datei wurde erfolgreich konvertiert: {output_filename}")
