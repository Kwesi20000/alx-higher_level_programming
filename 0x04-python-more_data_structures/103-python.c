#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints information about a Python list
 * @p: A pointer to the Python list object
 */
void print_python_list(PyObject *p) {
    if (PyList_Check(p)) {
        /* Get the size of the list */
        Py_ssize_t size = PyList_Size(p);
        PyObject *item;

        /* Print list information */
        printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %ld\n", size);
        printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

        /* Iterate through the list and print element types */
        for (Py_ssize_t i = 0; i < size; i++) {
            item = PyList_GetItem(p, i);
            printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
        }
    } else {
        /* Handle the case where the input is not a valid list */
        printf("[*] Python list info\n");
        printf("  [ERROR] Invalid List Object\n");
    }
}

/**
 * print_python_bytes - Prints information about a Python bytes object
 * @p: A pointer to the Python bytes object
 */
void print_python_bytes(PyObject *p) {
    if (PyBytes_Check(p)) {
        /* Get the size and string data of the bytes object */
        Py_ssize_t size = PyBytes_GET_SIZE(p);
        char *str = PyBytes_AsString(p);

        /* Print bytes object information */
        printf("[.] bytes object info\n");
        printf("  size: %ld\n", size);
        printf("  trying string: %s\n", str);

        printf("  first %ld bytes: ", size <= 10 ? size : 10);
        /* Print the first few bytes of the bytes object */
        for (Py_ssize_t i = 0; i < size && i < 10; i++) {
            printf("%02hhx", str[i]);
            if (i < size - 1 && i < 9)
                printf(" ");
        }
        printf("\n");
    } else {
        /* Handle the case where the input is not a valid bytes object */
        printf("[.] bytes object info\n");
        printf("  [ERROR] Invalid Bytes Object\n");
    }
}
