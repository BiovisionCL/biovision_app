
import 'package:flutter/material.dart';

class Footer extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Container(
      padding: EdgeInsets.all(24),
      color: Colors.black,
      alignment: Alignment.center,
      child: Text(
        '© 2025 Biovision. Todos los derechos reservados.',
        style: TextStyle(color: Colors.white),
      ),
    );
  }
}
