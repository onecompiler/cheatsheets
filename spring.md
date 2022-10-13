---
title: Spring 
description: Spring is a java web framework
created: 2022-10-13
updated: 2022-10-13
---

Spring is a complete and modular framework for developing enterprise applications in java.

Abides Hollywood Principle --> "Don't call us, we'll call you!"

![Java Frameworks](https://user-images.githubusercontent.com/60386381/169201186-29699fca-57e1-4293-adf6-320350008299.png)

### Features
- Open source
- Light weight
- Comprehensive
- Framework of frameworks
- Array of resources

### Advantages
- Simplicity
    - Because it's non-invasive, i.e., not coupled with any technology
    - Uses POJO (Plain Old Java Object) or POJI (Plain Old Java Interface)
- Testability
    - Has integrated testing frameworks like JUnit.
- Java is loosely coupled and so is Spring

### Architecture / Module List
![Architecture or Module List](https://user-images.githubusercontent.com/60386381/169217351-2bf7e492-df19-4195-badf-8c64f73fed21.png)

## Model View Controller (MVC)
![MVC](https://user-images.githubusercontent.com/60386381/169265090-eff4bb08-0bbc-4f16-866a-d8568528422a.png)

### Model
- Contains your data
- Data can be any Java object or collection

### View template
- Spring MVC is flexible
    - Supports multiple view templates
    - Most common is JSP(Java Server Pages) + JSTL(JSP Standard Tag Library)
    - Other templates:
        - Thymeleaf
        - Groovy
        - Velocity
        - Freemaker
- Displays data

### Controller
- Contains the business logic
    - Handles the request
    - Store and retrieve data
    - Place data in model
- Send appropriate view template
- Uses `@Controller` annotation

### Development Process
1. Model
    ```java
    // customer class
    public class Customer {
        @NotNull(message="Is required")
        @Size(min=2, message="Min name size should be of length 2")
        private String firstName;

        private String lastName;

        @Min(value = 1, message="Should be greater than 0")
        @Max(value = 10, message="Should be lesser than or equal to 10")
        private int freePasses;

        @NotNull(message="Is required")
        @Pattern(regexp="^[1-9][0-9]{5}", message="Postal Code should be of length 6")
        private Integer postalCode;

        // getter and setter methods
        ...
    }
    ```

2. Form or View Template (Input)
    ```JSP
    <!--customer-form.jsp-->
    <%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
    <!--Add HTML and BODY and STYLE tags -->
    <form:form action="processForm" modelAttribute="customer">
        First Name(*): <form:input path="firstName" />
        <form:errors path="firstName" cssClass="error" />

        <br/>

        Last Name: <form:input path="lastName" />

        <br/>

        Free Passess: <form:input path="freePasses" />
        <form:errors path="freePasses" cssClass="error" />

        <br/>

        Postal Code(*): <form:input path="postalCode" />
        <form:errors path="postalCode" cssClass="error" />

        <input type="submit" value="Submit" />
    </form:form>
    ```

3. Controller class
    ```java
    //customer controller class
    @Controller
    @RequestMapping("/customer")
    public class CustomerController {

        // Adding initbinder to trim the whitespaces
        @InitBinder
        public void initBinder(WebDataBinder db) {
            StringTrimmerEditor editor = new StringTrimmerEditor(true);

            db.registerCustomEditor(String.class, editor);
        }

        @RequestMapping("/showForm")
        public String showForm(Model model) {
            model.addAttribute("customer", new Customer());

            return "customer-form";
        }

        @RequestMapping("/processForm")
        public String processForm(@Valid @ModelAttribute("customer") Customer customer, BindingResult bindingResult) {
            if(bindingResult.hasErrors()) {
                return "customer-form";
            }
            return "customer-confirmation";
        }
    }
    ```

4. Confirmation page or View Template (Resultant)
    ```JSP
    <!--customer-confirmation.jsp-->
    <!DOCTYPE html>
    <html>
        <head>
            <title>Customer Confirmation</title>
        </head>
        <body>
            Customer: ${customer.firstName} ${customer.lastName}
            Passes: ${customer.freePasses}
            Postal Code: ${customer.postalCode}
            Course Code: ${customer.courseCode}
        </body>
    </html>