



# divide string into array of extensions
extensions_str = "php, .php2, .php3, .php4, .php5, .php6, .php7, .phps, .phps, .pht, .phtm, .phtml, .pgif, .shtml, .htaccess, .phar, .inc, .hphp, .ctp, .module"
extensions_list = [ext.strip() for ext in extensions_str.split(',')]

print(extensions_list)
