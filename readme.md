# CROP Images with CLI
Crops images with python using Pillow. Useful for cropping multiple images at the same time.
The dafult resolution is 1920x1080


## How to install
1. Install [pipx](https://github.com/pypa/pipx)
2. Install crop
```sh
pipx install crop
```

## How to use:
<details>
  <summary>Base Image</summary>

  ![image](examples/kanagawa.jpg)

</details>

1. Single file

```sh
crop examples/kanagawa.jpg -height 300 -width 300
```
<details>
  <summary>Output Focused 300x300</summary>

  ![image](examples/kanagawa-300x300.jpg)

</details>

3. Resize image to keep maximum information possible

```sh
crop examples/kanagawa.jpg -height 450 -width 450 -resize
```
<details>
  <summary>Output: resized then 450x450, </summary>

  ![image](examples/kanagawa-450x450.jpg)

</details>

1. Using ratio instead of size, will get biggest possible:

```sh
crop examples/kanagawa.jpg -ratio 1:1  
```
<details>
  <summary>Output: 2990x2990</summary>
    
  ![image](examples/kanagawa-2990x2990.jpg)

</details>


4. Make it recursive

```sh
crop -r {folder} -height {height} -width {width}
```