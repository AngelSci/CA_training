# Accessing Resources

### GitHub
You have full access to github via a Anaconda Enterprise Notebooks terminal just like you do from your local terminal.
Generate SSH keys from your Anaconda Enterprise Notebooks account and add them to your github account and you are ready to go.

<a href="https://help.github.com/articles/generating-ssh-keys" target="_blank">Generating GitHub SSH keys</a>

*Note:* The GitHub instructions recommend using pbcopy to add ~/.ssh/id_rsa.pub to your clipboard. Anaconda Enterprise Notebooks does not have pbcopy, so you'll need to do the following:

	$ cat ~/.ssh/id_rsa.pub
	# Then select and copy the contents of that file to your clipboard.
