# install flask -v 2.1.0

exec { 'Installing flask v 2.1.0':
  command => 'pip3 install flask==2.1.0',
}
