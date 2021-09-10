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
                <input type="file" name="pdf1"><br><br>
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
                    
                    $allowed = array('ppt','pptx');
                
                    if(in_array($fileActualExt, $allowed)){
                        if($fileErr === 0){
                            if($fileSize < 204800){
                                $fileNameNew = uniqid('',true).'.'.$fileActualExt;
                                $_SESSION['file1'] = $fileNameNew;
                                $exploded = explode('.',$_SESSION['file1']);
                                $final = 'convertedToPdf/'.$exploded[0].'.'.$exploded[1].'.pdf';
                                $destination = 'uploads/'.$fileNameNew;
                                move_uploaded_file($fileTmpName, $destination);
                                // echo "Upload Succesful File 1.<br>";
                            }else{
                                echo "Your file is too large. Select something under 20 MB <br>";
                            }
                        }else{
                            echo "There was some error uploading the file. <br>";
                        }
                    }else{
                        echo "File type unsupported. Please upload a file with a '.ppt' Extension <br>";
                    }
                    $cmd = "python3 converters/ppt-to-pdf.py ".$_SESSION['file1'];
                    // echo $cmd;
                    shell_exec($cmd);
                    echo "<br><a href='{$final}'>Download Converted pdf.</a>";
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