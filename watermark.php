<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Merge PDF</title>
    <link rel="stylesheet" href="style.css">
    <link rel="stylesheet" href="mergepdf.css">
</head>

<body>
    <div class="mergepdf" style="background: #202020;">
        <div class="header">

            <div class="menubar">
                <div class="logo">LOGO</div>
                <div class="menus">
                    <ul>
                        <li><a href='/'>Home</a></li>
                        <li><a>About</a></li>
                        <li><a href="#services">Services</a></li>
                        <li><a>Contact us</a></li>
                    </ul>
                </div>
            </div>

            <div class="mergepdf-header">
                <h2>Merge PDF files</h2>
                <p>Combine PDFs in the order you want with the easiest PDF merger available.</p>
            </div>
            <div class="mergepdf-form">
                <form action="" method="post" enctype="multipart/form-data">
                <div class='form-wrapper'>
                <label>Pdf file to add watermark to : </label><br><br>
                <input type="file" name="pdf1"><br><br>
                <label>Input the Watermark in .pdf format below : </label><br><br>
                <input type="file" name="pdf2"><br><br>
                <?php
               session_start();
               if(isset($_POST['submit'])){
                   $file = $_FILES['pdf1'];
               
                   $fileName = $_FILES['pdf1']['name'];
                   $fileTmpName = $_FILES['pdf1']['tmp_name'];
                   $fileSize = $_FILES['pdf1']['size'];
                   $fileErr = $_FILES['pdf1']['error'];
                   $fileType = $_FILES['pdf1']['type'];
               
                   $fileExt = explode('.',$fileName);
                   $fileActualExt = strtolower(end($fileExt));
                   
                   $allowed = array('pdf');
               
                   if(in_array($fileActualExt, $allowed)){
                       if($fileErr === 0){
                           if($fileSize < 204800){
                               $fileNameNew = uniqid('',true).'.'.$fileActualExt;
                               $_SESSION['file1'] = $fileNameNew;
                               $destination = 'uploads/'.$fileNameNew;
                               move_uploaded_file($fileTmpName, $destination);
                            //    echo "Upload Succesful File 1.<br>";
                           }else{
                               echo "Your file is too large. Select something under 20 MB <br>";
                           }
                       }else{
                           echo "There was some error uploading the file. <br>";
                       }
                   }else{
                       echo "File type unsupported. Please upload a file with a '.pdf' Extension <br>";
                   }
               
                   $file2 = $_FILES['pdf2'];
               
                   $file2Name = $_FILES['pdf2']['name'];
                   $file2TmpName = $_FILES['pdf2']['tmp_name'];
                   $file2Size = $_FILES['pdf2']['size'];
                   $file2Err = $_FILES['pdf2']['error'];
                   $file2Type = $_FILES['pdf2']['type'];
               
                   $file2Ext = explode('.',$file2Name);
                   $file2ActualExt = strtolower(end($file2Ext));
               
                   if(in_array($file2ActualExt, $allowed)){
                       if($file2Err === 0){
                           if($file2Size < 204800){
                               $file2NameNew = uniqid('',true).'.'.$file2ActualExt;
                               $_SESSION['file2'] = $file2NameNew;
                               $destination = 'uploads/'.$file2NameNew;
                               move_uploaded_file($file2TmpName, $destination);
                            //    echo "Upload Succesful File 2.";
                           }else{
                               echo "Your file is too large. Select something under 20 MB <br>";
                           }
                       }else{
                           echo "There was some error uploading the file2. <br>";
                       }
                   }else{
                       echo "File type unsupported. Please upload a file2 with a '.pdf' Extension <br>";
                   }
                   $cmd = "python3 converters/watermark.py ".$_SESSION['file1'].' '.$_SESSION['file2'].' '.$_SESSION['file1'];
                   shell_exec($cmd);
                   echo "<br><a href='watermarked/{$_SESSION['file1']}'>Download watermarked PDF.</a>";
               }
                ?>
                </div>
                    <br>
                    <button type="submit" name="submit" class="btn">Upload</button>
                </form>
            </div>
        </div>
    </div>
</body>

</html>