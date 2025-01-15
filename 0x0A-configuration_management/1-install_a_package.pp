#Using Puppet, install flask from pip3

# ensure python is present 
package { 'python3.8':
  ensure => present,
}

# ensure pip is present
package { 'python3-pip':
  ensure => present,
}

# Install Flask 
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip',
  require  => Package['python3-pip'],
}
