# 0x0A. CONFIGURATION MANAGEMENT

This repository is home to all files required for successful completion of the Configuration management provided by ALX Africa to its Software Engineering program.

## SUMMARY

Server configuration management (also popularly referred to as IT Automation) is a solution for turning one's infrastructure administration into a codebase, describing all processes necessary for deploying a server in a set of provisioning scripts that can be versioned and easily reused. It can greatly improve the integrity of any server infrastructure over time.

## REQUIREMENTS

# GENERAL

	->	All files will be interpreted on.
			Ubuntu 20.04 LTS
	->	All files should end with a new line
	->	A README.md file at the root of the folder of the project is mandatory
	->	Puppet manifests must pass
			puppet-lint
			version 2.1.1
				without any errors
	->	Puppet manifests must run without error
	->	Puppet manifests first line must be a comment explaining what the Puppet manifest is about
	->	Puppet manifests files must end with the extension:
			.pp

## NOTE ON VERSIONING

Ubuntu 20.04 VM should have Puppet 5.5 preinstalled.

### INSTALL PUPPET

	$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
	$ apt-get install -y ruby-augeas
	$ apt-get install -y ruby-shadow
	$ apt-get install -y puppet

No need to attempt to upgrade versions. This project is simply a set of tasks to familiarize one with the basic level syntax which is virtually identical in newer versions of Puppet.

### Install puppet-lint
	$ gem install puppet-lint