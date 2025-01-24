input_files = [f'{i}/{i}.tex' for i in range(1, 22 + 1)]
begin = r'\begin{document}'
end = r"\end{document}"

with open("/home/user_name/VScodeProjects/MethodsOfOptimization/old_questions/combined/old_combined.tex", 'w', encoding='utf-8') as outfile:
    outfile.write('\documentclass[17pt]{extarticle}\n')
    outfile.write(r"\usepackage{../mystyle}" + '\n')

    outfile.write(begin + '\n')

    for infile_name in input_files:
        try:
            with open(infile_name, 'r', encoding='utf-8') as infile:
                content = infile.read()
                
                content = content[content.index(begin):]
                content = content.replace(begin, '')
                content = content.replace(end, '')

                outfile.write(content)
                outfile.write('\n')
            print(f'Успешно добавлен файл: {infile_name}')
        except FileNotFoundError:
            print(f'Предупреждение: файл {infile_name} не найден. Пропускаем.')

    outfile.write(end + '\n')
