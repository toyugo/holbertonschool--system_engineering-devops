# Update

file_line {'pwd off':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no',
}

file_line { 'authfile':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/holberton',
}

