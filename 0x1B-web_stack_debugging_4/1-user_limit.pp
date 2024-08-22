# fix_holperton_user_hard

exec { "fix_holperton_user_hard":
  command => "sed -i '/^holberton/s/5/5000/' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/'
}

# fix_holperton_user_soft
exec { "fix_holperton_user_soft":
  command => "sed -i '/^holberton/s/4/5000/' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/'
}
