import 'package:flutter/material.dart';
import 'package:mobbanking/pages/login.dart';
import 'package:mobbanking/pages/signup.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const LogInPage(),
      routes: <String, WidgetBuilder>{
        '/login': (BuildContext context) => const LogInPage(),
        '/signup': (BuildContext context) => const Signup(),
      },
    );
  }
}
