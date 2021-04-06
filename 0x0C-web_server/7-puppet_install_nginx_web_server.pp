# puppet manifest
file {'Update index':
    ensure 	=> file,
    path	=> '/var/www/html/index.nginx-debian.html',
    content     => 'Holberton School',
}

