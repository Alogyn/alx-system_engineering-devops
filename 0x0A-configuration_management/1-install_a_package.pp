# Install an especific version of flask (2.1.0)
exec { 'install-flask':
  command => 'pip3 install flask==2.1.0',
  unless  => 'pip3 freeze | grep flask==2.1.0',
  path    => ['/bin', '/usr/bin', '/usr/local/bin'],
}
