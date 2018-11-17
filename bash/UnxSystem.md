# Unix System Configurations

## Check for mount devices
```
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