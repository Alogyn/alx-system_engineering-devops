# This Puppet manifest creates a file at /tmp/school with specific owner, group, permissions, and content

file { '/tmp/school':
  ensure  => file,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  content => 'I love Puppet',
}

