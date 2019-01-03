# Unix System Configurations

## Check for mount devices
```
    $ lsblk
    $ df -h
```

## Check available devices
```
    $ fdisk -l
```

## Modify device format / partition
```
    $ fdisk /dev/your-device
```

## Format devices
```
    $ mkdosfs /dev/your-device
```

- Format to FAT32
```
    $ umount /dev/your-device
    $ sudo mkdosfs -I -F32 /dev/your-device

    $ sudo mkfs.vfat -I /dev/your-devices
```

- Format to exFat
- Requires additional packages to format
```
    $ sudo dnf install fuse-exfat exfat-utils
    $ sudo mkfs.exfat /dev/your-device

```

## Delete partition on device
```
    $ fdisk /dev/your-device
```
    - Type `d` to delete a partition
    - Type `1` to select 1st partition

## Check disk partition label
```
    $ fdisk -l -u
```

# How to format SD card to FAT32
- Using tool called `parted`
- Select device to partition
```
    $ sudo parted /dev/your-device
```

- Create partition table
```
    (parted) $ mklabel msdos
```

- Create partitions on device
- This cmd creates one partition
```
    (parted) $ mkpart primary fat32 1MiB 100%
    (parted) $ set 1 boot on
    (parted) $ quit
```

- Format as FAT32
```
    $ sudo mkfs.vfat /dev/your-device-partition
```

# User Groups
- Check user groups
```
    $ cut -d: -f1 /etc/group
```