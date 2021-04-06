# puppet manifest
file {'Update index':
    ensure 	=> present,
    path	=> '/var/www/html/index.html',
    content     => 'Holberton School\n',
}
file_line { 'adjust redirect':
    path  => '/etc/nginx/sites-enabled/default',
    line  => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
    match => '# pass .*',
}
