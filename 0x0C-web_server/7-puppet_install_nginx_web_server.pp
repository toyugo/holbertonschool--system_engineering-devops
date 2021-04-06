# puppet manifest
file {'Update index':
    ensure 	=> file,
    path	=> '/var/www/html/index.html',
    content     => 'Holberton School\n',
}

