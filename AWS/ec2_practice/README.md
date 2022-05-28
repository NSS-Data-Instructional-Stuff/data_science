# AWS EC2 Exercise
In this exercise, you will get to practice interacting with an AWS ec2 instance using ssh and get to learn some new command line tools.

**Note:** Before doing this exercise, you'll want to make sure that jupyter is not running on your computer. If it is and you cannot close it, you'll have the change the port numbers in step 2 below.

**Note 2:** The installation steps need to be run only once per group.

1. Step 1 - Before you can connect you need to change the permissions on the key pair file that you will use to connect through ssh. This is done using the `chmod` command. Specifically, we will set the permissions level to 400, which is read permission and no other permissions. For more information about `chmod`, see [this page.](https://www.tutorialspoint.com/unix_commands/chmod.htm) To do this, navigate to the location of your `.pem` file and run

`chmod 400 mykeys.pem`

2. Next, you will connect to your ec2 instance using `ssh`, the secure shell protocol. What this will look like is 

`ssh -i "mykeys.pem" -L 8888:localhost:8888 ubuntu@<DNS>`

Breaking down what this does, we are first pointing ssh to our private key file with the -i flag. The -L flag sets forwards the 8888 port on our local machine to the 8888 port on the localhost of the ec2 instance. The purpose of this is to allow us to connect to a jupyter notebook running on the ec2 instance. Finally, we need to specify the DNS of the ec2 instance we are connecting to.

The first time you do this, you will get a warning message that the authenticity of the host can't be established and will ask you to verify that you want to continue connecting.

3. Once you have successfully connected, we need to set up our instance in order to be able to use Python and the libraries we need. One way to do this is to install the miniconda distribution of Anaconda, which is a smaller version. We can then use our environment.yml file to install exactly what we will need.
To do this, since we are working from the command line on the remote machine, we can make use of `curl`, a command line tool for transferring data with urls. 

To use curl, you can run 

`curl <url to fetch> --output <file to save the result into>`

Using your local machine, navigate to the miniconda downloads page (https://docs.conda.io/en/latest/miniconda.html) and find the url for the latest installer of Miniconda3 (64 bit) for Linux. This will be the url to fetch. You can sub this url into the above command. Next, you need to choose a filename to save the results into. This will retrieve a bash script for installing miniconda, so I recommend calling it something simple, like `mc.sh`.

4. After downloading the installer, we need to run it. This can be done by running

`bash mc.sh`

After installing, you'll need to exit and reconnect. This can be done by typing `exit`, which will return you to your normal shell. Then you can reconnect using the same `ssh` call as above. Once you reconnect, you can verify that conda was installed if you run the following command and don't get an error:

`conda --v`

5. After reconnecting, we need to install the libraries that you will need. I have set up a yml file containing the necessary packages and versions, but we need a way to get it from your local machine over to the ec2 instance. For this, we can use `scp`, the secure copy protocol. **This step needs to be run on a new terminal instance on your local machine.** The command you need to run looks like

`scp -i "mykeys.pem" <file to copy> ubuntu@<DNS>:~/.`

6. Once you have copied the yml file over, create a conda environment using it.

7. Finally, we're going to be interacting with files on AWS s3. This can be made easier if we install the AWS cli on our ec2 machine. To do this, we're going to use `apt`, the Advanced Package Tool. First we need to update it:

`sudo apt update`

Then, we can install the AWS cli using

`sudo apt install awscli`

Finally, we can configure it with our credentials by running

`aws configure`

and giving the access key id and secret access key that I shared with you.

8. We are finally ready to work in jupyter. Make sure that you have activated the environment that you installed and then launch jupyter. Open your browser (on your local machine) and navigate to the url displayed.

9. There is a file that is contained in the `nss-ds5` bucket on `s3` at the address `s3://nss-ds5/data/Metro_Credit_Card_Transactions.csv`. Read this file into a pandas dataframe. (To get the file to your ec2 instance, you can use the AWS cli, boto3, or just use `read_csv` and point to the file, which is possible by using the `s3fs` library.) Once you have done this, find the top 4 merchants by total `Transaction Amount` for the metro police deparment. Create some kind of visualization for this and export your result to a `png` file with your group's name in the file name.

10. Finally, exit jupyter and make use of the AWS cli to copy your png file to the `nss-ds5` bucket into the `images` folder. See https://docs.aws.amazon.com/cli/latest/reference/s3/cp.html if you need help with this.