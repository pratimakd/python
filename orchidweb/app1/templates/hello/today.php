<!DOCTYPE HTML>	
<html>

<head>
	<style>
		.error{
			color: red;
		}
		</style>
<title> creating a form</title>
</head>

<body>
	<?php
	 $errName=$errparentname=$erremail=$errgender=' ';
	 $name=$parentname=$email=$gender=' ';
	if(isset($_POST['submit'])){
		$name=$_POST['username'];
		$parentname=$_POST['parents'];
		$email=$_POST['email'];
	
		
		if(empty($name)){
			$errName="Name should not be empty";
			
		}
		else{
			echo $name;
			echo "<br>";
	}
	if(empty($parentname)){
		$errparentname= "parentname should not be empty";
	}
	else{
		echo $parentname;
		echo "<br>";
	}
	if(empty($email))
        {
           $erremail="Email is empty". "<br>";
		
        }
        else{
            if(filter_var($email,FILTER_VALIDATE_EMAIL))
            {
                echo $email;
				echo "<br>";
            }
            else{
                $erremail="email is not in proper format"."<br>";
            }
        }
       if(empty($_POST['Gender']))
       {
   
			$errgender= "gender is empty";
		}
		else{
			echo $gender;
		}

	}
?>
<form method="POST" action="<?php echo $_SERVER['PHP_SELF']?>">
	<table border="1px solid black">
		<tr>
			<td> Full Name</td>
			<td> <Input type="text" name="username"></td>
			<span class="error"><?php echo $errName ?> </span>
		</tr>
		<tr>
			<td>Parents Name</td>
			<td><input type="text" name="parents"></td>
			<span class="error"><?php echo $errparentname?> </span>
			
			<tr>
			<td>Email ID</td>
			<td><input type="text" name="email"></td>
			<span class="error"> <?php echo $erremail?> </span>
		</tr>
		
		<tr>
			
		<td>Gender</td>
		<td>
			<input type="radio" name="Gender" value="male">Male<br>
			<span class="error"> <?php $errgender ?> </span>
			<input type="radio" name="Gender" value="Female">FeMale<br> 
			<span class="error"> <?php $errgender ?> </span>
			<input type="radio" name="Gender" value="others">Others<br> 
			<span class="error"> <?php $errgender ?> </span>
		</td>
	</tr>
	<tr>
		<td>Date of birth</td>
		<td>
			<select year="year">
				<option value="year">Year</option>
				<?php 
				for($i=1970;$i<=2022;$i++)
				{
					echo "<option value=$i>$i</option>";

				}

				?>
			</select>
			<select month="month">
				<option value="month">month</option>
				<?php
				for($i=1;$i<=12;$i++)
				{
					echo "<option value=$i>$i</option>";
				}
			?>
			
			</select>
				<select day="day">
					<option value="day">Day</option>
				<?php
				for($i=1;$i<=32;$i++)
				{
					echo "<option value=$i>$i</option>";
					
				}
				?>
				</select>
				</td>
			</tr>
			<tr>
				<td>faculty</td>
				<td>
					 <input type="checkbox" name="BIM[]" value="BIM">BIM<br>
            <input type="checkbox" name="BSW[]" value="BSW">BSW<br>
            <input type="checkbox" name="BBA[]" value="BBA" >BBA<br>
             <input type="checkbox" name="CSIT[]" value="CSIT" >CSIT<br>
              <input type="checkbox" name="BBM[]" value="BBM" >BBM<br>
               <input type="checkbox" name="BBS[]" value="BBS" >BBS
           </td>
       </tr>
       <tr>
     
       		<td>Shift</td>
       		<td><input type="radio" name="morning" value="morning">Morning<br>
       			<input type="radio" name="Day" value="Day">Day<br>
       			</td>
       		</tr>
       		<tr>
       			<td>website:</td>
       			<td><input type="text" name="name"></td>
       		</tr>
       		<tr>
       			<td>Feedback</td>
       			<td><textarea name="comment" cols="10" rows="6"></textarea>
       			</td>
       		</tr>
       		<tr>
       			<td colspan="2">
       				<input type="checkbox" name="click" value="click">I accept all the terms and conditions.</td>
       			</tr>
       			<tr>
       				<td>
       					<input type="submit" name="submit" value="send">
       					<input type="Reset" name="Reset" value="Reset">
       					</td>
       				</tr>
 </pre>
 </table>
	</form>


</body>
</html>