# Frequently Asked Questions

<div class="panel-group" id="accordion">
  <div class="panel panel-default">
    <div class="panel-heading">
      <h4 class="panel-title">
        <a class="accordion-toggle" data-toggle="collapse" data-parent="#accordion" href="#q1">
Q: What is Anaconda Enterprise Notebooks?
        </a>
      </h4>
    </div>
    <div id="q1" class="panel-collapse collapse">
      <div class="panel-body">
        <p>
A: Anaconda Enterprise Notebooks is a browser-based data analytics and visualization tool.  Anaconda Enterprise Notebooks is available as a private install within your Enterprise.
Each Anaconda Enterprise Notebooks node is configured with an extensive Python development environment using Anaconda from Continuum Analytics.
With Anaconda Enterprise Notebooks you can view, edit, and share Jupyter notebooks.
      </p>
      </div>
    </div>
  </div>
  <div class="panel panel-default">
    <div class="panel-heading">
      <h4 class="panel-title">
        <a class="accordion-toggle" data-toggle="collapse" data-parent="#accordion" href="#q2">
Q: How can I access my data from Anaconda Enterprise Notebooks?
       </a>
      </h4>
    </div>
    <div id="q2" class="panel-collapse collapse">
      <div class="panel-body">
        <p>
A: If your data is in csv files, we recommend uploading the csv files to your Anaconda Enterprise Notebooks account.
If your data is stored in Amazon S3 you can access it directly from your Anaconda Enterprise Notebooks scripts using the boto package and IOPro.
If your data is in
      </p>
      </div>
    </div>
  </div>
  <div class="panel panel-default">
    <div class="panel-heading">
      <h4 class="panel-title">
        <a class="accordion-toggle" data-toggle="collapse" data-parent="#accordion" href="#q3">
Q: Can I install other Python packages? How?
       </a>
      </h4>
    </div>
    <div id="q3" class="panel-collapse collapse ">
      <div class="panel-body">
        <p>
A: The root environment is read-only and can only be changed by a system administrator.  This guarantees a consistent root environement
for everyone using Anaconda Enterprise Notebooks.  When you need a custom environment you can create an environment within your project.  See the documentation
on creating project environments for more information.
      </p>
      </div>
    </div>
  </div>
  <div class="panel panel-default">
    <div class="panel-heading">
      <h4 class="panel-title">
        <a class="accordion-toggle" data-toggle="collapse" data-parent="#accordion" href="#q4">
Q: Can I create my own Python environments?
       </a>
      </h4>
    </div>
    <div id="q4" class="panel-collapse collapse ">
      <div class="panel-body">
        <p>
A: Yes. Using the conda command from the shell prompt, you can create new Python environments and include whatever packages you choose.
All Anaconda Enterprise Notebooks environments are shared with all the team members of a project.
This is a powerful and unique feature of Anaconda Enterprise Notebooks.  See the Project Environments section for more information.
      </p>
      <p>
      	An example conda create command that will create an environement called myenv.  The environment will contain the numpy package:
      	<code>conda create -n myenv numpy</code>
      </p>
      <p>python, ipython and pip are installed by default in all new envs in Anaconda Enterprise Notebooks.</p>
      </div>
    </div>
  </div>
  <div class="panel panel-default">
    <div class="panel-heading">
      <h4 class="panel-title">
        <a class="accordion-toggle" data-toggle="collapse" data-parent="#accordion" href="#q5">
Q: Is it possible to get a print view of my IPython notebooks?
       </a>
      </h4>
    </div>
    <div id="q5" class="panel-collapse collapse ">
      <div class="panel-body">
        <p>
A: Yes. Although our IPython notebook does not currently have a print view, you should be able to print your notebooks using your browser's regular printing capabilities.
      </p>
      </div>
    </div>
  </div>
  <div class="panel panel-default">
    <div class="panel-heading">
      <h4 class="panel-title">
        <a class="accordion-toggle" data-toggle="collapse" data-parent="#accordion" href="#q7">
Q: How much storage do I get?
       </a>
      </h4>
    </div>
    <div id="q7" class="panel-collapse collapse ">
      <div class="panel-body">
        <p>
A: There is no set limit for storage - this is limited only by the size of the disk where Anaconda Enterprise Notebooks is installed.  If you are having storage issues, please contact your system administrator.
      </p>
      </div>
    </div>
  </div>
  <div class="panel panel-default">
    <div class="panel-heading">
      <h4 class="panel-title">
        <a class="accordion-toggle" data-toggle="collapse" data-parent="#accordion" href="#q8">
Q: What should I do if Anaconda Enterprise Notebooks isn't functioning properly?
       </a>
      </h4>
    </div>
    <div id="q8" class="panel-collapse collapse ">
      <div class="panel-body">
        <p>
A: Try refreshing the page first. If that does not resolve the issue, try closing and reopening the application that is not functioning properly.

If that does not resolve the issue, you can restart your project by navigating to Project Settings icon -> Project tab -> Controls section and Pause and then Start your project.

If that does not work, ensure that you are using the latest version of your web browser (Chrome, Safari, or Firefox). Then log out, restart your browser, and log back in.

If you continue to have issues, then please <a href="mailto:support@continuum.io">e-mail us</a>.
      </p>
    </div>
  </div>
  <div class="panel panel-default">
    <div class="panel-heading">
      <h4 class="panel-title">
        <a class="accordion-toggle" data-toggle="collapse" data-parent="#accordion" href="#q11">
Q: How do I suggest features that should be added?
       </a>
      </h4>
    </div>
    <div id="q11" class="panel-collapse collapse ">
      <div class="panel-body">
        <p>
A: Send an email with your suggestions to <a href="mailto:support@continuum.io">support@continuum.io</a>.
      </p>
      </div>
    </div>
  </div>
  <div class="panel panel-default">
    <div class="panel-heading">
      <h4 class="panel-title">
        <a class="accordion-toggle" data-toggle="collapse" data-parent="#accordion" href="#q12">
  </div>
</div>
