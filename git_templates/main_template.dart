import 'package:flutter/material.dart';
import 'core/widgets/navbar.dart';
import 'core/widgets/footer.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Biovision',
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        body: Container(
          decoration: BoxDecoration(
            image: DecorationImage(
              image: AssetImage("assets/images/background.jpg"),
              fit: BoxFit.cover,
            ),
          ),
          child: Column(
            children: [
              NavigationBar(),
              Expanded(child: Center(child: Text("Contenido principal"))),
              FooterWidget(),
            ],
          ),
        ),
      ),
    );
  }
}