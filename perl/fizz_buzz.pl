#!/usr/local/bin/perl -w

=head1 DESCRIPTION

Prints the numbers from 1 to 100. But for multiples of three print 'Fizz'
instead of the number and for the multiples of five print 'Buzz'. For numbers
which are multiples of both three and five print 'FizzBuzz'.

=cut

for my $i (1 .. 100) {
    if ($i % 15 == 0) {
        print "FizzBuzz\n";
    }
    elsif ($i % 3 == 0) {
        print "Fizz\n";
    }
    elsif ($i % 5 == 0) {
        print "Buzz\n";
    }
    else {
        print "$i\n";
    }
}
