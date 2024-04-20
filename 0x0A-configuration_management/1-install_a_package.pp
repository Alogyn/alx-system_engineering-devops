# Install an especific version of flask (2.1.0)
exec { 'install-flask':
  command => 'pip3 install Flask==2.1.0',
  unless  => 'pip3 freeze | grep Flask==2.1.0',
  path    => ['/bin', '/usr/bin', '/usr/local/bin'],
}
