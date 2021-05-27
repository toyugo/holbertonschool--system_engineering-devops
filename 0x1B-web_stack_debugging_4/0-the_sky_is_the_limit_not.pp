# Puppet script
exec { 'Add_open_file_cache':
  command => 'sed -i "s/# server_tokens off;/open_file_cache max=200000/" /etc/nginx/nginx.conf',
  path    => '/usr/local/bin/:/bin/'
}

-> exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
