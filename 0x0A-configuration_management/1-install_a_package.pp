#Install a package
class { 'python3': }
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}
exec { 'python-installed':
  command => '/usr/bin/which python3',
}