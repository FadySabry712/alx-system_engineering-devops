# find out why Apache is returning a 500 error
# fix it and then automate it using Puppet instead of using Bash

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
