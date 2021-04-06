# puppet manifest
file {'Update index':
    ensure 	=> present,
    path	=> '/var/www/html/index.html',
    content     => 'Holberton School\n',
}
