import stylecloud

ip_files = ('top_authors_2019.csv', 'top_authors_2021.csv')
op_files = ('top_authors_2019.png', 'top_authors_2021.png')

for ip_file, op_file in zip(ip_files, op_files):
    stylecloud.gen_stylecloud(file_path=ip_file,
                              icon_name='fas fa-book-open',
                              background_color='black',
                              gradient='horizontal',
                              output_name=op_file)
