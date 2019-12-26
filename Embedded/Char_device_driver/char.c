#include <linux/init.h>
#include <linux/module.h>
#include <linux/device.h>
#include <linux/kernel.h>
#include <linux/fs.h>
#include <linux/uaccess.h>

#define DEVICE_NAME "Kushagra"
#define CLASS_NAME "abc"

MODULE_LICENSE("GPL");

static int major; 
static char msg[256] = {0};
static short len;
static struct class *kushClass = NULL;
static struct device *kushDevice = NULL;

static int dev_open(struct inode*, struct  file *);
static int dev_release(struct inode*, struct  file *);
static ssize_t dev_read(struct file *, char *, size_t, loff_t *);
static ssize_t dev_write(struct file *, const char *, size_t, loff_t *);

static struct file_operations fops = {
.open = dev_open,
.read = dev_read,
.write = dev_write,
.release = dev_release,
};

int kushchar_init(void) {
	printk(KERN_INFO "kushagra device init");
	major = register_chrdev(0, DEVICE_NAME, &fops);
	if (major < 0) {
		printk(KERN_INFO "kushagra device init failed");
		return major;
	}

	// Register the device class
	kushClass = class_create(THIS_MODULE, CLASS_NAME);
	if (IS_ERR(kushClass)) {
		printk(KERN_INFO "kushagra failed to register class");
		unregister_chrdev(major, DEVICE_NAME);
		return PTR_ERR(kushClass);
	}
	printk(KERN_INFO "kushagra registered class");

	// register the device driver
	kushDevice = device_create(kushClass, NULL, MKDEV(major, 0), 
			NULL, DEVICE_NAME);
	if (IS_ERR(kushDevice)) {
		printk(KERN_INFO "kushagra failed to register class");
		class_destroy(kushClass);
		unregister_chrdev(major, DEVICE_NAME);
		return PTR_ERR(kushDevice);
	}
	printk(KERN_INFO "kushchar registered class and device");
	return 0;
}

void kushchar_exit(void) {
	printk(KERN_INFO "kushchar device unloaded");
	device_destroy(kushClass, MKDEV(major, 0));
	class_unregister(kushClass);
	class_destroy(kushClass);
	unregister_chrdev(major, DEVICE_NAME);
}

static int dev_open(struct inode *inodep, struct file *filep) {
	printk(KERN_INFO "kushchar device opened");
	return 0;
}

static ssize_t dev_read(struct file *filep, char *buffer, size_t len, loff_t *offset){
   // copy_to_user has the format ( * to, *from, size) and returns 0 on success
   int error;
   error = copy_to_user(buffer, msg, len);
 
   if (error==0){
      printk(KERN_INFO "Sent characters to the user\n");
      return 0;
   }
   else {
      printk(KERN_INFO "Failed to send characters to the user\n");
      return -EFAULT;     
   }
}

static ssize_t dev_write(struct file *filep, const char *buffer, size_t len, loff_t *offset){
   sprintf(msg, "%s(%zu letters)", buffer, len);
   len = strlen(msg);
   printk(KERN_INFO "Received %zu characters from the user\n", len);
   return len;
}
 
static int dev_release(struct inode *inodep, struct file *filep){
   printk(KERN_INFO "Device closed\n");
   return 0;
}
 
module_init(kushchar_init);
module_exit(kushchar_exit);

