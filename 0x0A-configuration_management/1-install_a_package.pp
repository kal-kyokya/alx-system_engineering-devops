# Ensure Python 3 and pip3 are installed
package { 'python3':
  ensure => installed,
}

package { 'python3-pip':
  ensure => installed,
}

# Install Flask using pip3 with a specific version
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}