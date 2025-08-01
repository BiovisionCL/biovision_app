import 'package:flutter/material.dart';

class CustomNavigationBar extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Container(
      height: 60,
      color: Colors.blueGrey[900],
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceAround,
        children: [
          Text('Biovision', style: TextStyle(color: Colors.white, fontSize: 20)),
          TextButton(onPressed: () {}, child: Text("Inicio", style: TextStyle(color: Colors.white))),
          TextButton(onPressed: () {}, child: Text("Servicios", style: TextStyle(color: Colors.white))),
          TextButton(onPressed: () {}, child: Text("Contacto", style: TextStyle(color: Colors.white))),
        ],
      ),
    );
  }
}