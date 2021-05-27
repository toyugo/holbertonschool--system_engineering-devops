# Increase hard file limit
exec { 'increase_hard':
  command => 'sed -i "s/nofile 5/100000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

# Increase soft file limitr.
exec { 'increase_soft':
  command => 'sed -i "s/nofile 4/100000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
