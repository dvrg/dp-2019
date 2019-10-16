# Bahan Ajar Desktop Programming 2019
Materi pembelajaran Python untuk AMCC divisi Desktop Programming 2019

### Pertemuan 1
1. (Git)[]
2. (Bash/Terminal)[]
3. (SSH)[]

#### SSH
Untuk melakukan pembuatan `SSH Key`, ikutin langkah-langkah berikut:
1. Buka terminal (Linux) dan GitBash (Windows)
2. ketikan `ssh-keygen` maka akan muncul pertanyaan seperti dibawah ini, hal ini memastikan tempat dimana `SSH Key` disimpan, tekan <kbd>Enter</kbd> untuk menyimpan secara default.
```
Generating public/private rsa key pair.
Enter file in which to save the key (/home/genpati/.ssh/id_rsa):
```
3. lalu muncul pertanyaan seperti ini, artinya, pengguna diminta untuk memasukan kata kunci khusus untuk `SSH Key` yang akan di buat, tekan <kbd>Enter</kbd> untuk menyimpan secara default.
```
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
```
4. kamu berhasil membuat `SSH Key`
```
Your identification has been saved in /home/genpati/.ssh/id_rsa.
Your public key has been saved in /home/genpati/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:xxXXx/xXxXU5hHgGQEGVCI7Y2IDDjoBie8joq0XxXx genpati@genpati
The key's randomart image is:
+---[RSA 3072]----+
|#@.+.            |
|&.*.o  .         |
|**x=... .        |
|o=*..x.  .       |
|+o o.  .S.       |
|.oo     o        |
|+XX. . .         |
|+.o.. .          |
|..xX.            |
+----[SHA256]-----+

```
5. menambahkan `SSH Key` ke akun GitHub bisa ikuti caranya [disini][1]
6. copy `SSH Key` dengan cara `cat ~/.ssh/id_rsa.pub` lalu select dan copy isi yang muncul pada terminal
7. masuk ke akun github, lalu ke profile > settings > SSH & GPG > Add Key, lalu paste `SSH Key` yang sudah di copy lalu Save Key
---
Sumber :

[https://help.github.com/en/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent](https://help.github.com/en/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

[1]:https://help.github.com/en/articles/adding-a-new-ssh-key-to-your-github-account
