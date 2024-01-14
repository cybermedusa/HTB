import subprocess

# divide string into array of extensions
extensions_str = ".pHp, .pHP5, .PhAr, .php, .php2, .php3, .php4, .php5, .php6, .php7, .phps, .phps, .pht, .phtm, .phtml, .pgif, .shtml, .htaccess, .phar, .inc, .hphp, .ctp, .module"
extensions_list = [ext.strip() for ext in extensions_str.split(',')]

base_file_name = "zipped_pdf.pdf"

for extension in extensions_list:
    subprocess.run(['touch', base_file_name+extension])


