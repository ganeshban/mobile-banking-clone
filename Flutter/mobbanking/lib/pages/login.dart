import 'dart:convert';
import 'dart:async';

import 'package:flutter/material.dart';
import 'package:mobbanking/utils/http_request.dart';

class LogInPage extends StatefulWidget {
  const LogInPage({Key? key}) : super(key: key);

  @override
  State<LogInPage> createState() => _LogInPageState();
}

class _LogInPageState extends State<LogInPage> {
  TextEditingController username = TextEditingController(text: "username");
  TextEditingController password = TextEditingController(text: "password");
  String message = '';

  void doLogin(String uid, String psw) async {
    var api = ApiRequest('http://127.0.0.1', '8000');
    api.addPath('login');
    api.addQuery('username=' + uid);
    api.addQuery('password=' + psw);
    var data = await api.get();
    print(data);
    data = jsonDecode(data);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('My Appbar'),
      ),
      body: Column(
        children: [
          const FlutterLogo(size: 150.0),
          TextField(
            controller: username,
          ),
          TextField(
            controller: password,
          ),
          TextButton(
              onPressed: () {
                doLogin(username.text, password.text);
              },
              child: const Text("Login")),
          Text(message.isEmpty ? '' : message)
        ],
      ),
    );
  }
}
