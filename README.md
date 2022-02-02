# moodle-email-converter

Small python script I wrote for my former job as student assistant. It can be used to extract names from a .csv file and convert them into a list of valid university email addresses.
The script could be used to generate a list for moodle course enrollments, if only a list of names is present.

The script provides two options to generate the email address. It can either use an table with separate columns for the first and last name or extract the information out of one combined field using a regex pattern. 
