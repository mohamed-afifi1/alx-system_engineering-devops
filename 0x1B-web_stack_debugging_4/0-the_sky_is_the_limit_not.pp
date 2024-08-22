# ulimit 4096 instead of 15

exec { 'fix ulimit':
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin:/bin',
}

exec { 'restart nginx':
  command => '/etc/init.d/nginx restart',
  path    => '/etc/init.d',
}
