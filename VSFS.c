#include <stdio.h> //std io
#include <sys/types.h> //fork
#include <sys/xattr.h> // xattr
#include <sys/stat.h> //stat
#include <sys/acl.h> // acl
#include <stdlib.h> //char *
#include <pwd.h> //passwd
#include <dirent.h> //dirent
#include <grp.h> //group
#include <time.h> //tm
#include <string.h> //string
#include <unistd.h>
#include <limits.h>

#define GetCurrentDir getcwd
#define NONE_FS ""

void attribute(mode_t file_mode){
    /* Check whether it is directory */
    if (S_ISDIR(file_mode)) printf("d");
    else printf("-"); 

    /* Check r permission of the owner */
    if (file_mode & S_IRUSR) printf("r");
    else printf("-");

    /* Check w permission of the owner */
    if (file_mode & S_IWUSR) printf("w");
    else printf("-");

    /* Check x permission of the owner */
    if (file_mode & S_IXUSR) printf("x");
    else printf("-");

    /* Check r permission of the group */
    if (file_mode & S_IRGRP) printf("r");
    else printf("-");

    /* Check w permission of the group */
    if (file_mode & S_IWGRP) printf("w");
    else printf("-");

    /* Check x permission of the group */
    if (file_mode & S_IXGRP) printf("x");
    else printf("-");

    /* Check r permission of the others */
    if (file_mode & S_IROTH) printf("r");
    else printf("-");

    /* Check w permission of the others */
    if (file_mode & S_IWOTH) printf("w");
    else printf("-");

    /* Check x permission of the others */
    if (file_mode & S_IXOTH) printf("x");
    else printf("-");
}

const char* month_int_to_string(int month) {
    char* month_to_string = "";
    switch(month) {
        case 1:
            month_to_string = "Jan";
            break;
        case 2:
            month_to_string = "Feb";
            break;
        case 3:
            month_to_string = "Mar";
            break;
        case 4:
            month_to_string = "Apr";
            break;
        case 5:
            month_to_string = "May";
            break;
        case 6:
            month_to_string = "Jun";
            break;
        case 7:
            month_to_string = "Jul";
            break;
        case 8:
            month_to_string = "Aug";
            break;
        case 9:
            month_to_string = "Sep";
            break;
        case 10:
            month_to_string = "Oct";
            break;
        case 11:
            month_to_string = "Nov";
            break;
        case 12:
            month_to_string = "Dec";
            break;
    }
    return month_to_string;
}

void list(char* FS){
    struct passwd* owner; // for pw_name
    DIR* directory; // for current directory
    struct dirent* directory_entry; // for directory entry
    struct group* group; // for gr_name
    struct stat file_info; // for file information
    mode_t file_mode; // for type and permission of file
    struct tm* created_time; // for the time file created
    char* file_path_and_name;
    int total_size = 0;

    /* Set the directory */
    if (FS[strlen(FS)-1] == '/') {
        int size = strlen(FS);
        FS[size-1] = '\0';
    }

    /* Set the directory */
    directory = opendir(FS);
    if (directory == NULL) {
        perror("Error ");
        exit(1);
    }

    /* Check the total size of directory */
    while (directory_entry = readdir(directory)) {
        if (stat(directory_entry -> d_name, &file_info) == -1) {
            printf("%s\n", directory_entry -> d_name);

            perror("Error ");
            exit(1);  
        }
        if (!(directory_entry -> d_name[0] == '.')) {
            total_size += file_info.st_size;
        }
    }

    /* Print directory */
    printf("%s:\n", FS);

    /* Print total size */
    printf("total %d\n", total_size/1000);

    directory = opendir(FS);

    /* Read files one by one */
    while (directory_entry = readdir(directory)) {
        if (stat(directory_entry -> d_name, &file_info) == -1) {
            printf("%s\n", directory_entry -> d_name);

            perror("Error ");
            exit(1);  
        }
        /* Check whether it is hidden file */
        if (!(directory_entry -> d_name[0] == '.')) {
            file_mode = file_info.st_mode;

            /* Print attribute */
            attribute(file_mode);

            /* Print acl */
            file_path_and_name = (char *)malloc(1 + strlen(FS) + strlen("/") + strlen(directory_entry -> d_name));
            if (acl_get_file(file_path_and_name, ACL_TYPE_ACCESS) != 0) printf("+ ");
            else printf(" ");  

            /* Print the number of link */
            printf("%3ld ", file_info.st_nlink);

            /* The owner of file */ 
            owner = getpwuid(file_info.st_uid);
            /* The group of the file */
            group = getgrgid(file_info.st_gid);
            /* Print the owner and group */
            printf("%s ", owner->pw_name);
            printf("%s ", group->gr_name);

            /* Print the size of file */
            printf("%ld ", file_info.st_size);

            /* The time file created */
            created_time = localtime(&(file_info.st_mtime));
            int month = created_time->tm_mon+1;
            printf("%s %d %02d:%02d ", month_int_to_string(month), created_time->tm_mday, created_time->tm_hour, created_time->tm_min);

            /* The note name */
            printf("%s/", FS);
            if(directory_entry->d_ino != 0) printf("%s\n", directory_entry->d_name );
        }
    }
    closedir(directory);
}

void invalid_message() {
    fprintf(stderr, "Invalid VSFS\n");
    exit(1);
}

int main(int argc, char* argv[]) {
    if ((argc != 3) && (argc != 4) && (argc != 5)) {
        invalid_message();
    }
    else {
        if (strcmp(argv[1], "list") == 0) {
            if (argc == 3) {
                char* FS = argv[2];
                list(FS);
            }
            else {
                invalid_message();
            }
        }
        else if (strcmp(argv[1], "copyin") == 0) {

        }
        else if (strcmp(argv[1], "copyout") == 0) {
            
        }
        else if (strcmp(argv[1], "mkdir") == 0) {
            
        }
        else if (strcmp(argv[1], "rm") == 0) {
            
        }
        else if (strcmp(argv[1], "rmdir") == 0) {
            
        }
        else if (strcmp(argv[1], "defrag") == 0) {
            
        }
        else if (strcmp(argv[1], "index") == 0) {
            
        }
        else {
            
        }
    }
    return EXIT_SUCCESS;
}