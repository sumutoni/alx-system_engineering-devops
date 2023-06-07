# There is a typ in a php file so the website returns 500
exec { 'sed -i s@.phpp @.php @ /var/www/html/wp-settings.ph':
  command => 'sed  -i "s@.phpp@.php@" /var/www/html/wp-settings.php',
  path    => ['/bin','/sbin','usr/bin','usr/sbin'],
}
