import 'package:flutter/material.dart';

class LogInPage extends StatelessWidget {
  const LogInPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('My Appbar'),
      ),
      body: Column(
        children: const [
          FlutterLogo(size: 150.0),
          Text('User Name'),
          Text('password')
        ],
      ),
    );
  }
}
